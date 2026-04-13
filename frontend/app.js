const API_URL = 'https://crypto-dashboard-rvy9.onrender.com'

async function fetchCryptos() {
  try {
    const response = await fetch(`${API_URL}/cryptos/`)
    
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`)
    }

    const cryptos = await response.json()
    renderCards(cryptos)
    renderChart(cryptos)
    
    document.getElementById('last-updated').textContent = 
      `Last updated: ${new Date().toLocaleTimeString()}`

  } catch (error) {
    console.error('Error fetching cryptos:', error)
  }
}

function renderCards(cryptos) {
  const container = document.getElementById('cards-container')
  container.innerHTML = cryptos.map(crypto => `
    <div class="col-md-4">
      <div class="card">
        <div class="card-body">
          <h6 class="text-secondary">${crypto.symbol}</h6>
          <h4 class="fw-bold">$${crypto.price_usd.toLocaleString()}</h4>
          <p class="text-secondary small">
            Market Cap: $${(crypto.market_cap / 1e9).toFixed(2)}B
          </p>
        </div>
      </div>
    </div>
  `).join('')
}

function renderChart(cryptos) {
  const ctx = document.getElementById('price-chart').getContext('2d')
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: cryptos.map(c => c.symbol),
      datasets: [{
        label: 'Price (USD)',
        data: cryptos.map(c => c.price_usd),
        backgroundColor: ['#f7931a', '#627eea', '#9945ff']
      }]
    },
    options: {
      plugins: { legend: { labels: { color: '#e6edf3' } } },
      scales: {
        x: { ticks: { color: '#e6edf3' } },
        y: { ticks: { color: '#e6edf3' } }
      }
    }
  })
}

fetchCryptos()
setInterval(fetchCryptos, 30000)