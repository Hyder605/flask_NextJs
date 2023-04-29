'use client'
import { useEffect, useState } from "react"

export default function Home() {
  const [data, setData]=useState({})
  useEffect(()=>{
    fetch('/analyze').then(
      res=>res.json()
    ).then(
      data=>{
        setData(data)
        console.log(data)
      }
    )
  },[])

  return (

    <div>
      hello
    </div>
  )
    
  
}
