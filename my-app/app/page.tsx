async function getData() {
  const res = await fetch('https://brown-tailor-cralo.ineuron.app:5000/users');
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.

  // Recommendation: handle errors
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error('Failed to fetch data');
  }

  return res.json();
}

export default async function Home() {

  const quote = await getData();
  console.log(quote.Analyzed_Data)
  
  return (
    <div>
          <div>Number of Rows : {quote.Analyzed_Data[0].num_rows}</div>
          <div>Number of Rows : {quote.Analyzed_Data[0].num_cols}</div>


    </div>
    
  )
}