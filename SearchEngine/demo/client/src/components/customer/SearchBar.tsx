import { useEffect, useState } from "react";

type Props = {
  resultSetter: (res: []) => void;
};

export default function SearchBar({ resultSetter }: Props) {
  const [query, setQuery] = useState("");

  const handleQueryChange = (e: any) => {
    setQuery(e.target.value);
  };
  const handleSearch = async (e: any) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8082/search", {
        method: "POST",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ search: query }),
      });
      const data = await response.json();
      resultSetter(data.cars);
    } catch (err) {}
  };

  return (
    <div className=" sticky top-0 col-span-6 grid grid-cols-6 bg-[#f8f8f8] bg-opacity-90">
      <h1 className="col-span-6 m-6 ml-10 text-4xl font-bold">Customer Page</h1>
      <input
        value={query}
        onChange={handleQueryChange}
        placeholder="Un coche rojo para la montaña ..."
        className="inlin-block bottom-2 col-span-2 ml-10 rounded-xl border-2 border-blue-400 py-3 pl-6 pr-8 shadow-md "
      />
      <button
        onClick={handleSearch}
        className="tansition-all ml-4 w-12 items-center justify-center rounded-xl bg-blue-300 text-center align-middle duration-200 hover:scale-110 hover:bg-blue-400"
      >
        <svg
          className="mx-auto h-8 w-8 text-white"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          strokeWidth="2"
          stroke="currentColor"
          fill="none"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          {" "}
          <path stroke="none" d="M0 0h24v24H0z" />{" "}
          <circle cx="10" cy="10" r="7" />{" "}
          <line x1="21" y1="21" x2="15" y2="15" />
        </svg>
      </button>
      <hr className="col-span-6 mx-2 mr-10 mt-6  text-cyan-200" />
    </div>
  );
}
