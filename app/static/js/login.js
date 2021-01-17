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