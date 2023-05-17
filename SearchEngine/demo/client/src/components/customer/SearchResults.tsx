import { useEffect } from "react";
import CarCard from "./CarCard";

type Props = {
  results: any;
};
export default function SearchResults({ results }: Props) {
  useEffect(() => {
    console.log(results);
  }, []);

  return (
    <div className="col-span-6 mx-10 grid grid-cols-1 grid-rows-6 md:grid-cols-2  lg:grid-cols-3">
      {results.length === 0 && (
        <h1 className="col-start-2 row-start-4  text-center align-middle text-6xl font-bold text-slate-400 opacity-80">
          Busca algo!
        </h1>
      )}
      {results.map((d: any) => (
        <div className="bg-base-100 col-span-1 my-4 inline-block w-96 rounded-xl border-2 p-6 shadow-xl">
          {Object.entries(d).map(([key]) => (
            <>
              <span key={d[key]} className="block">
                <b key={d[key]}>{key}</b>: {d[key]}
              </span>
            </>
          ))}
        </div>
      ))}
    </div>
  );
}

/**
 *  <span key={d[key]} className="block">
                <b key={d[key]}>{key}</b>: {d[key]}
              </span>
 */
