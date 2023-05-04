import React, { useState } from "react";
import axios from "axios";

function App() {
  let [query, setQuery] = useState("");
  let [result, setResult] = useState([]);

  let [auto, setAuto] = useState(false);

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
        <h1 className="font-bold text-4xl">WW Search Engine Demo</h1>
        <span>© NL Search Engine by WheelWise™</span>
      </div>
      <div className="md:col-span-3 col-span-5 col-start-2 md:col-start-3">
        <input
          type="text"
          placeholder="Un carro rojo ..."
          className="input input-bordered input-primary w-full max-w-xs"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
          }}
        />
        <button onClick={search} className="btn btn-outline btn-success mx-2">
          Buscar
        </button>
        <div><button onClick={()=> {setAuto(!auto); setQuery(query + " automatico")}} className={`hover:bg-slate-300 bg-slate-200 ${auto ? "bg-blue-400" : ""} py-2 px-3 rounded-xl my-2`}>X automatico</button></div>
      </div>

      <div className="col-span-6 grid grid-cols-6 m-8 mt-12">
        {result.map((d) => (
          <div className="card col-span-2 w-96 bg-base-100 shadow-xl border-2 my-4">
            <div className="card-body">
              <h2 className="card-title text-2xl">
                {d.marca + "  " + d.modelo}
              </h2>
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
