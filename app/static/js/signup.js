const signup = document.getElementById("sign-up");
const signupGoogle = document.getElementById("sign-up-google");

signup.onclick = (e) => {
  const emailElement = document.getElementById("email");
  const passwordElement = document.getElementById("password");
  const zipElement = document.getElementById("zip");

  const email = emailElement.value;
  const password = passwordElement.value;
  const zip = zipElement.value;
  
  console.log('Create User on firebase');
  e.preventDefault();
  fetch(
      '/api/register', 
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          email,
          password,
          zip_code: zip
        })
      }
  )
  .then(resp => resp.json())
  .then(data => {
    console.log(data)
    console.log('User is registered go to login page')
    //TODO
  })
  .then(_=> firebase.auth().signInWithEmailAndPassword(email, password))
  .then(_=> firebase.auth().currentUser.getIdToken(true))
  .then(idToken=> {
    document.cookie = `id_token=${idToken}`;
    location.href = '/';
  })
  .catch(error=>console.error(error));

  return false;
};

signupGoogle.onclick = (e) => {
  firebase.auth().signInWithRedirect(googleAuthProvider);
  return false;
};

firebase.auth()
  .getRedirectResult()
  .then((result) => {
    if (result.credential) {
      /** @type {firebase.auth.OAuthCredential} */
      //var credential = result.credential;

      // This gives you a Google Access Token. You can use it to access the Google API.
      //var token = credential.accessToken;
      // ...

      // This does nothing because I don't think it's worth it to have two register pages
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