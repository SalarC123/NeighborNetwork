const login = document.getElementById("login");
const loginGoogle = document.getElementById("login-google");

login.onclick = (e) => {
  const emailElement = document.getElementById("email");
  const passwordElement = document.getElementById("password");

  const email = emailElement.value;
  const password = passwordElement.value;
  
  console.log('Login User on firebase');
  e.preventDefault();
  firebase.auth().signInWithEmailAndPassword(email, password)
  .then(_=> firebase.auth().currentUser.getIdToken(true))
  .then(idToken=> {
    document.cookie = `id_token=${idToken}`
    return fetch(
      '/api/user', 
      {
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      })
    })
  .then(resp => resp.json())
  .then(user=>{
    console.log(user);
    console.log('User is logged in go to login page');
    location.href = '/';
  })
  .catch(error=>{
    console.error(error)
    // Should delete the cookie if expired
  });

  return false;
};

loginGoogle.onclick = (e) => {
  firebase.auth().signInWithRedirect(googleAuthProvider);
  return false;
};

firebase.auth()
  .getRedirectResult()
  .then((result) => {
    if (result.credential) {
      /** @type {firebase.auth.OAuthCredential} */
      var credential = result.credential;

      // This gives you a Google Access Token. You can use it to access the Google API.
      var token = credential.accessToken;
      // ...

    }
    // The signed-in user info.
    var user = result.user;
  }).catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    // The email of the user's account used.
    var email = error.email;
    // The firebase.auth.AuthCredential type that was used.
    var credential = error.credential;
    // ...
  });