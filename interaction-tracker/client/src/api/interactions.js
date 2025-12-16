const API_BASE = 'http://127.0.0.1:8000/api'; // adjust port if needed


export async function createInteraction(data) {
  const res = await fetch(`${API_BASE}/interactions`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new Error(`Failed to create interaction: ${res.status}`);
  }
  
  return res.json();
}

export async function getInteractions(params = {}) {
  const query = new URLSearchParams(params).toString();
  const res = await fetch(`${API_BASE}/interactions?${query}`);
  return res.json();
}

export async function getStats() {
  const res = await fetch(`${API_BASE}/interactions/stats`);
  return res.json();
}
