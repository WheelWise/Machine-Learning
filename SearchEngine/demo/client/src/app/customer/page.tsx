"use client";
import { SearchBar, SearchResults } from "@/components/customer";
import { useState } from "react";

export default function Customer() {
  const [reuslt, setResult] = useState([]);
  return (
    <main className="grid grid-cols-6 gap-3 text-gray-800">
      <SearchBar resultSetter={setResult} />
      <SearchResults results={reuslt} />
    </main>
  );
}
