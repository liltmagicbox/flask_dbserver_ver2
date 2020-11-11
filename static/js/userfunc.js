function fetchnewuser(){
  let username = document.getElementById("username").value
  let sha = sha256(encodeURI( document.getElementById("sha").value ))
  let params = { 'username': username, 'sha': sha,}
  let url = window.location.href.split(window.location.pathname)[0]
  let fetchurl = url+'/fetchnewuser'
fetch(fetchurl,
{
  method: 'POST', // or 'PUT'
  body: JSON.stringify(params), // data can be `string` or {object}!
  headers:{
    'Content-Type': 'application/json'
  }
})
//.then( function(response){return response.json()})
.then( response => response.json() )
.then(function(myJson){
  let rawText = myJson['bodytext']
  //console.log(rawText)

  let a = document.createElement('p')
  a.innerText = rawText
  document.body.appendChild(a)
  alert(rawText)

})

}

function fetchlogin(){
  let username = document.getElementById("username").value
  let sha = sha256(encodeURI( document.getElementById("sha").value ))
  //let sha = document.getElementById("sha").value

  let params = { 'username': username, 'sha': sha,}
  let url = window.location.href.split(window.location.pathname)[0]
  let fetchurl = url+'/fetchlogin'

//fetch(fetchurl, {method: 'POST', body: JSON.stringify( params )} )
fetch(fetchurl,
{
  method: 'POST', // or 'PUT'
  body: JSON.stringify(params), // data can be `string` or {object}!
  headers:{
    'Content-Type': 'application/json'
  }
})

//.then( function(response){return response.json()})
.then( response => response.json() )
.then(function(myJson){
  //let rawText = myJson['bodytext']
  //console.log(rawText)
  let username = myJson['username']
  let token = myJson['token']
  document.cookie = "username="+username
  document.cookie = "token="+token

  if(token=='no'){ alert('뭔가 문제가..!')}
  else{
  username.disabled=true
  sha.disabled=true
  let fetchnewuserB = document.getElementById("fetchnewuserB")
  fetchnewuserB.hidden=true
  let fetchloginB = document.getElementById("fetchloginB")
  fetchloginB.hidden=true
  let fetchlogoutB = document.getElementById("fetchlogoutB")
  fetchlogoutB.hidden=false
  }
})

}

function fetchlogout(){
  username.disabled=false
  sha.disabled=false
  /*
  let fetchnewuserB = document.getElementById("fetchnewuserB")
  fetchnewuserB.hidden=false
  let fetchloginB = document.getElementById("fetchloginB")
  fetchloginB.hidden=false
  let fetchlogoutB = document.getElementById("fetchlogoutB")
  fetchlogoutB.hidden=true
  */
  document.cookie = "username=no"
  document.cookie = "token=no"
  window.location.reload()
}




function makeloginbox(outframe){
  let logincontents =`
  asdfwefwef
  `
}
