import {get,set} from 'js-cookie'
// const _endpoint = 'http://localhost:5000/api/'
let endpoint = ''

//http://stackoverflow.com/a/8809472/3842656
const generateUUID = () => {
    var d = new Date().getTime()
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now() //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0
        d = Math.floor(d/16)
        return (c=='x' ? r : (r&0x3|0x8)).toString(16)
    })
    return uuid
}


const getAnonId = () => {
  let anonId = get('anonId')
  if(!anonId){
    anonId = generateUUID()
    set('anonId', anonId)
  }
  return anonId
}

const getContext = () => ({
    url: window.location.href,
    path: window.location.pathname,
    referrer: document.referrer,
    title: document.title,
    context_user_agent: navigator.userAgent,
    sent_at: Date.now().toString(),
})

const page = extraData => {

  const user_id = get('gsId')
  const anonymous_id = getAnonId()

  let data = {
    user_id,
    anonymous_id,
  }

  Object.assign(data, getContext())
  Object.assign(data, extraData)

  console.log(data)

  const xhr = new XMLHttpRequest()
  xhr.open("POST", window.ra.endpoint + "/page/")
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8")
  xhr.send(JSON.stringify(data))
}

const identify = gsID => {
  set('gsID', gsID)
}


window.ra = {page, endpoint, identify}
