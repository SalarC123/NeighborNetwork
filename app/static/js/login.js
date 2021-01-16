const login = document.getElementById("login");

login.onclick = (e) => {
  const emailElement = document.getElementById("email");
  const passwordElement = document.getElementById("password");

  const email = emailElement.value;
  const password = passwordElement.value;
  
  console.log('Login User on firebase');
  e.preventDefault();
  firebase.auth().signInWithEmailAndPassword(email, password)
  .then(_=> firebase.auth().currentUser.getIdToken(true))
  .then(idToken=> fetch(
      '/api/user', 
      {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Authorization': `Bearer ${idToken}`
        }
      }))
  .then(resp => resp.json())
  .then(user=>{
    console.log(user)
    console.log('User is logged in go to login page')
    //TODO
  })
  .catch(error=>console.error(error));

  return false;
};