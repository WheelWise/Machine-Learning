import { useState } from "react";

type Props = {
  onNext: () => void;
  onCancel: (e: any) => void;
  fileId: string;
  attributes: never[];
  viewSetter: (v: object) => void;
  makeSetter: (m: string) => void;
};

export default function StepTwo({
  onNext,
  onCancel,
  fileId,
  viewSetter,
  attributes,
  makeSetter,
}: Props) {
  const [viewForm, setViewForm] = useState({ title: "", year: "", price: "" });
  const [makeInput, setMakeInput] = useState("");

  const handleTitle = (e: any) => {
    e.preventDefault();
    setViewForm((prevView) => ({ ...prevView, title: e.target.value }));
  };

  const handleYear = (e: any) => {
    e.preventDefault();
    setViewForm((prevView) => ({ ...prevView, year: e.target.value }));
  };

  const handlePrice = (e: any) => {
    e.preventDefault();
    setViewForm((prevView) => ({ ...prevView, price: e.target.value }));
  };

  const handleMake = (e: any) => {
    e.preventDefault();
    setMakeInput(e.target.value);
  };

  const handleSubmit = () => {
    const allValuesNotEmpty = Object.values(viewForm).every(
      (value) => typeof value === "string" && value.trim() !== ""
    );
    if (allValuesNotEmpty) {
      viewSetter(viewForm);
      makeSetter(makeInput);
      onNext();
      return;
    }
    return;
  };

  const cancelOverride = async (e: any) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8082/cancel", {
        method: "POST",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ file_id: fileId }),
      });
      const data = await response.json();
    } catch (err) {}
    onCancel(e);
  };
  return (
    <>
      <div className="col-span-6 ml-8 mr-2 grid grid-cols-2">
        <h2 className="col-span-2 text-xl font-bold text-slate-800">
          <svg
            className="mb-[0.2rem] mr-2 inline-block h-7 w-7"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            {" "}
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />{" "}
            <circle cx="8.5" cy="8.5" r="1.5" />{" "}
            <polyline points="21 15 16 10 5 21" />
          </svg>
          2. Configra la vista de tus autos.
        </h2>
        <div className="col-span-1 ">
          <p className="mb-2 text-slate-500">
            <span className="block text-xl font-bold text-emerald-500">
              Importante!
            </span>
            <i className="text-blue-600">Wheelie</i> ha analizado tu archivo y
            ha encontrado los atributos de tus vehiculos, ahora solo slecciona
            cuales de los atributos seran los que veran los clientes.{" "}
            <b className="text-pink-600">
              * Asegurate de configurar las vistas{" "}
            </b>
          </p>
          <label
            htmlFor="first_name"
            className="block text-sm font-medium text-gray-900 dark:text-white"
          >
            Marca
          </label>
          <input
            type="text"
            id="first_name"
            className="block w-[92%] rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
            placeholder="?"
            value={makeInput}
            onChange={handleMake}
            required
          ></input>
          <div className="inline-block w-[30%]">
            <label
              htmlFor="countries"
              className=" block text-sm font-medium text-gray-900 dark:text-white"
            >
              Titulo
            </label>
            <select
              onChange={handleTitle}
              id="countries"
              className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
            >
              <option value="">?</option>
              {attributes.map((data) => (
                <option key={data} value={data}>
                  {data}
                </option>
              ))}
            </select>
          </div>
          <div className="ml-2 inline-block w-[30%]">
            <label
              htmlFor="countries"
              className="block text-sm font-medium text-gray-900 dark:text-white"
            >
              Año
            </label>
            <select
              onChange={handleYear}
              id="countries"
              className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
            >
              <option value="">?</option>
              {attributes.map((data) => (
                <option key={data} value={data}>
                  {data}
                </option>
              ))}
            </select>
          </div>
          <div className="ml-2 inline-block w-[28%]">
            <label
              htmlFor="countries"
              className="inline-block text-sm font-medium text-gray-900 dark:text-white"
            >
              Precio
            </label>
            <select
              onChange={handlePrice}
              id="countries"
              className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
            >
              <option value="">?</option>
              {attributes.map((data) => (
                <option key={data} value={data}>
                  {data}
                </option>
              ))}
            </select>
          </div>
        </div>
        <div className="col-span-1 mx-8 grid grid-cols-6 rounded-lg border border-gray-300 bg-white shadow-md">
          <div className="col-span-6 mx-6 mb-2 mt-4 rounded-lg border-2 border-dashed border-slate-100 bg-slate-200 p-4 py-8 text-center">
            <i className="font-semibold text-slate-400">Foto del Vehiculo</i>
          </div>
          <h5 className="col-span-6 ml-6  text-xl font-semibold tracking-tight text-gray-900">
            {makeInput} {viewForm.title} {viewForm.year}
          </h5>
          <span className="col-span-6 -mt-10 ml-6 inline-block text-xl font-bold text-slate-700">
            $ {viewForm.price} MXN
          </span>
        </div>
      </div>
      <div className="col-span-6 row-start-6 mx-6 items-end  justify-end text-end ">
        <button
          onClick={cancelOverride}
          className={`mx-2 rounded-[2rem] border-2 border-slate-300 px-4 py-2 text-slate-400 transition-all duration-200 hover:border-red-400 hover:text-red-400 `}
        >
          Cancelar
        </button>
        <button
          onClick={handleSubmit}
          className="mx-2 rounded-[2rem] border-2 border-blue-500 px-4 py-2 text-blue-500 transition-all duration-200 hover:bg-blue-500 hover:text-white"
        >
          Continuar
        </button>
      </div>
    </>
  );
}
