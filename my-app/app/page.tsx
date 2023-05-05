'use client'
import { useState, useEffect } from 'react'

type ApiResponse = {
  message: string
}

export default function Home() {
  const [data, setData] = useState<ApiResponse | null>(null)

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('https://brown-tailor-cralo.ineuron.app:5000')
      const json = await response.json()
      setData(json)
    }
    fetchData()
  }, [])

  return (
    <div>{data?.message}</div>
  )
}


