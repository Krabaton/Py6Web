console.log('TODO App')

const form = document.forms[0]

addEventListener('submit', async (e) => {
  e.preventDefault()
  const response = await fetch('http://127.0.0.1:8000/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      username: form.username.value,
      password: form.password.value,
    }),
  })
  console.log(response.status)
  if (response.status === 200) {
    resultJson = await response.json()
    localStorage.setItem('token', resultJson.access_token)
    localStorage.setItem('email', resultJson.user_email)
    window.location = '/list-notes.html'
  }
})
