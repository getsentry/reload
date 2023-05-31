import { get, set } from "js-cookie";
// const _endpoint = 'http://localhost:5000/api/'
let endpoint = "";

// we want to make sure we don't create events with too large a size
// so we should trim any fields to this length or less
const MAX_FIELD_LENGTH = 2000;

const assign =
  Object.assign ||
  function (target) {
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
  console.warn("getAnonId is deprecated");
  return "";
};

// we want to use the referrer from the site that
// brought us here from the original_referrer query param
// which we store in a cookie since it will be lost on page navigation
const getOriginalReferrer = () => {
  try {
    const params = new URLSearchParams(window.location.search);
    const originalReferrer = params.get("original_referrer");
    return originalReferrer || document.referrer;
  } catch (err) {
    console.error(err);
  }
  return document.referrer;
};

const getContext = () => {
  const out = {
    url: window.location.href,
    path: window.location.pathname,
    referrer: getOriginalReferrer(),
    document_referrer: document.referrer,
    title: document.title,
    sent_at: Date.now().toString(),
  };
  // trim fields to prevent the payload from being too large
  for (let field in out) {
    out[field] = out[field].slice(0, MAX_FIELD_LENGTH);
  }
  return out;
};

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
  let data = {
    user_id,
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

const page = (extraData) => {
  send("/page/", extraData);
};

const identify = (gsID) => {
  set("gsID", gsID, { domain: getTLD() });
};

const metric = (name, value, tags) => {
  send(
    "/metric/",
    {
      metric_name: name,
      value,
      tags,
    },
    true
  );
};

window.ra = { page, event, endpoint, identify, getAnonId, metric };
