import { get, set } from "js-cookie";
// const _endpoint = 'http://localhost:5000/api/'
let endpoint = "";

//http://stackoverflow.com/a/8809472/3842656
const generateUUID = () => {
  var d = new Date().getTime();
  if (window.performance && typeof window.performance.now === "function") {
    d += performance.now(); //use high-precision timer if available
  }
  var uuid = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(
    c
  ) {
    var r = (d + Math.random() * 16) % 16 | 0;
    d = Math.floor(d / 16);
    return (c == "x" ? r : (r & 0x3) | 0x8).toString(16);
  });
  return uuid;
};

const assign =
  Object.assign ||
  function(target) {
    if (target === undefined || target === null) {
      throw new TypeError("Cannot convert undefined or null to object");
    }

    var output = Object(target);
    for (var index = 1; index < arguments.length; index++) {
      var source = arguments[index];
      if (source !== undefined && source !== null) {
        for (var nextKey in source) {
          if (source.hasOwnProperty(nextKey)) {
            output[nextKey] = source[nextKey];
          }
        }
      }
    }
    return output;
  };

const getTLD = () => {
  // For development environments
  if (["127.0.0.1", "0.0.0.0", "localhost"].indexOf(location.hostname) >= 0) {
    return location.host;
  }

  var parts = location.hostname.split(".");
  if (parts.length > 2) {
    parts.shift();
  }
  var upperleveldomain = parts.join(".");
  return upperleveldomain;
};

const getAnonId = () => {
  let anonId = get("anonId");
  if (!anonId) {
    anonId = generateUUID();

    set("anonId", anonId, { domain: getTLD() });
  }
  return anonId;
};

const getContext = () => ({
  url: window.location.href,
  path: window.location.pathname,
  referrer: document.referrer,
  title: document.title,
  sent_at: Date.now().toString()
});

const performXhrSend = (endpoint, data) => {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", endpoint);
  xhr.send(JSON.stringify(data));
};

let _batchThrottleId = null;
const performBatchSend = () => {
  if (_batchThrottleId) {
    return;
  }

  // Batch/throttle requests into 1 second interval
  _batchThrottleId = setTimeout(() => {
    // Clear _batchedData
    for (let key in _batchedData) {
      if (!_batchedData.hasOwnProperty(key)) {
        return;
      }

      // Currently can only batch by endpoint (and only /metrics/)
      performXhrSend(key, _batchedData[key]);
      _batchedData[key] = [];
    }
    _batchThrottleId = null;
  }, 1000);
};

const _batchedData = {};

const batchSend = (endpoint, data) => {
  if (!_batchedData[endpoint]) {
    _batchedData[endpoint] = [];
  }

  _batchedData[endpoint].push(data);
  performBatchSend();
};

const send = (path, extraData, batch) => {
  const user_id = get("gsID");
  const anonymous_id = getAnonId();
  let data = {
    user_id,
    anonymous_id
  };

  assign(data, getContext(), extraData);

  const sendFunc = !batch ? performXhrSend : batchSend;
  sendFunc(window.ra.endpoint + path, data);
};

const event = (name, extraData) => {
  let data = { event_name: name };
  assign(data, extraData);
  send("/event/", data);
};

const page = extraData => {
  send("/page/", extraData);
};

const identify = gsID => {
  set("gsID", gsID, { domain: getTLD() });
};

const metric = (name, value, tags) => {
  send(
    "/metric/",
    {
      metric_name: name,
      value,
      tags
    },
    true
  );
};

window.ra = { page, event, endpoint, identify, getAnonId, metric };
