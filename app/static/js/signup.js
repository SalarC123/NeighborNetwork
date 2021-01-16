const signup = document.getElementById("sign-up");

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
  ).then(data => {
    console.log(data)
    console.log('User is registered go to login page')
    //TODO
  }).catch(error=>console.error(error));

  return false;
};