import React, { useState } from "react";
import axios from "axios";

function App() {
  let [query, setQuery] = useState("");
  let [result, setResult] = useState([]);

  const search = () => {
    axios
      .post(
        "http://localhost:8080/search",
        { s: query },
        {
          headers: { "content-type": "application/x-www-form-urlencoded" },
        }
      )
      .then((response) => {
        setResult(response.data.cars);
      });
  };

  return (
    <div className="grid grid-cols-6">
      <div className="md:col-span-2 col-span-6 md:col-start-3 mt-8 mb-8">
        <h1 className="font-bold text-4xl">WW Search Engine Demo 😶‍🌫️</h1>
        <span>© NL Search Engine by WheelWise™</span>
      </div>

      <form className="md:col-span-2 col-span-5 col-start-2 md:col-start-3">
        <div class="relative">
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg
              aria-hidden="true"
              class="w-5 h-5 text-gray-500 dark:text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              ></path>
            </svg>
          </div>
          <input
            type="search"
            class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Buscar autos ..."
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
            }}
          />
          <button
            onClick={search}
            type="submit"
            class="transition-all duration-300 text-white absolute right-2.5 bottom-2.5 bg-indigo-600 hover:bg-indigo-800 hover:scale-110  font-medium rounded-lg text-sm px-4 py-2 "
          >
            Buscar
          </button>
        </div>
      </form>

      <div className="col-span-6 grid grid-cols-6 m-8 mt-12">
        {result.map((d) => (
          <div className="col-span-2 w-96 bg-base-100 shadow-xl border-2 my-4">
            <div className="">
              <h2 className="text-2xl">{d.marca + "  " + d.modelo}</h2>
              <ul>
                {Object.entries(d).map(([key, val]) => (
                  <li key={key}>
                    <b>{key}</b>: {val}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
