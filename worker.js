addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const baseURL = 'https://api.torob.com/v4/base-product/sellers/';
  const productID = 'b7fe3c1c-0d74-4a3a-bed3-7e29e92f3fda'; // نمونه productID
  const maxPages = 10; // تعداد صفحات مورد انتظار

  let results = [];

  for (let page = 1; page <= maxPages; page++) {
    const torobAPI = `${baseURL}?source=next_desktop&prk=${productID}&page=${page}`;
    
    try {
      const response = await fetch(torobAPI, {
        method: 'GET',
        headers: getHeaders()
      });

      if (response.ok) {
        const data = await response.json();
        console.log(`Page ${page} data:`, data); // چاپ داده‌های هر صفحه
        results = results.concat(data.items); // فرض بر این است که نتایج در `items` قرار دارد
      } else {
        throw new Error(`API request failed for page ${page}`);
      }
    } catch (error) {
      return new Response(`Error fetching data from Torob API: ${error.message}`, { status: 500 });
    }
  }

  return new Response(JSON.stringify(results), { status: 200 });
}

function getHeaders() {
  const headers = new Headers();
  headers.set('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3');
  headers.set('Accept-Language', 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7');
  headers.set('Referer', 'https://torob.com/');
  return headers;
}
