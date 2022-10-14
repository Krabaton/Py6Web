const url = new URL(window.location.href)
console.log(url)
const pattern = /\d+/gi
const [id] = url.pathname.match(pattern)

fetch(`${url.origin}/chart-info/${id}`).then(r => r.json()).then(result => {
    console.log(result)
    const labels = []
    const dataset = []
    console.log(result[result.length - 1])
    const title = Object.keys(result[result.length - 1])[1]
    console.log(title)
    for (let i = 0; i < result.length; i++) {
        for (const [key, value] of Object.entries(result[i])) {
            if (key === 'date') {
                labels[i] = value
            } else {
                dataset[i] = value
            }
        }
    }

    const data = {
        labels: labels,
        datasets: [{
            label: title,
            data: dataset,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            borderWidth: 1
        }]
    };
    const config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
    };
    ctx = document.getElementById('myChart').getContext('2d')
    new Chart(ctx, config)
})