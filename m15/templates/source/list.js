const main = async () => {
    token =  localStorage.getItem('token')
    if (token) {
        const response = await fetch('/notes', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        console.log(response.status)
        if (response.status === 200) {
            resultJson = await response.json()
            for (el of resultJson) {
                liHtml = document.createElement('li')
                liHtml.className = 'list-group-item'
                liHtml.textContent = `${el.id}: ${el.title} - ${el.description}. Status: ${el.done}. Date: ${el.created}`
                notes.appendChild(liHtml)
            }
        }
        if (response.status === 401) {
            window.location = '/'
        }
    }
}

main()