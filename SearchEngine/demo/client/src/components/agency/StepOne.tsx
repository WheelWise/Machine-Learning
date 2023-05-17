import { useState } from "react";

type Props = {
  onNext: () => void;
  onCancel: (e: any) => void;
  lineSetter: (l: number) => void;
  fileIdSetter: (id: string) => void;
};

export default function StepOne({
  onNext,
  onCancel,
  lineSetter,
  fileIdSetter,
}: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [isDragOver, setIsDragOver] = useState(false);
  const [error, setError] = useState(0);

  const handleDragEnter = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragOver(true);
  };

  const handleDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragOver(false);
  };

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    setFile(file);
  };

  const handleSubmit = async () => {
    switch (error) {
      case 0:
        if (file) {
          try {
            const form = new FormData();
            form.append("file", file);
            const response = await fetch("http://localhost:8080/upload", {
              method: "POST",
              body: form,
            });
            const data = await response.json();
            if (!data.error) {
              lineSetter(data.lines);
              fileIdSetter(data.id);
              onNext();
            } else {
              setError(2);
            }
          } catch (err) {
            setError(2);
          }
        }
        break;
      case 2:
        setFile(null);
        setError(0);
    }
  };

  const cancelOverride = (e: any) => {
    setFile(null);
    setError(0);
    onCancel(e);
  };
  return (
    <>
      {error === 0 && (
        <div className="col-span-6 grid grid-cols-2 ">
          <div className="col-span-1 ml-8 mr-2">
            <h2 className=" text-xl font-bold text-slate-800">
              <svg
                className="mb-1 mr-2 inline-block h-7 w-7"
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
                <path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2" />{" "}
                <polyline points="7 9 12 4 17 9" />{" "}
                <line x1="12" y1="4" x2="12" y2="16" />
              </svg>
              1. Sube tu catalogo
            </h2>
            <p className="mt-4 text-slate-500">
              Aqui puedes subir tu catalogo tal y como lo tienes,{" "}
              <i className="text-violet-600">Wheelie</i> lo aprendera por ti y
              se asegurara de que los clientes encuentren todo tus vechiculos!
              <br />
              <br />
              Puedes subir tu catalogo en un archivo csv o xls, ¡no importa la
              informacion que traiga! Solo asegurate que tenga una columna con
              el header <b className="text-red-400">modelo</b>.
            </p>
          </div>
          <div className="col-span-1 ">
            <div
              className={`z-1 mx-8 mt-10 h-[60%] rounded-md border-2 border-dashed  p-6 hover:bg-gray-200 ${
                file !== null
                  ? "border-green-400 bg-green-50 hover:bg-green-100"
                  : "border-gray-400 bg-gray-100 hover:bg-gray-200"
              }`}
              onDragEnter={handleDragEnter}
              onDragLeave={handleDragLeave}
              onDragOver={handleDragOver}
              onDrop={handleDrop}
              onClick={() => {
                const fileInput = document.querySelector(
                  "input[type=file]"
                ) as HTMLInputElement;
                fileInput.click();
              }}
            >
              {file ? (
                <p className="text-center align-middle  text-green-700">
                  <svg
                    className="mx-auto my-2 h-8 w-8 text-green-500"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    {" "}
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />{" "}
                    <polyline points="14 2 14 8 20 8" />{" "}
                    <line x1="16" y1="13" x2="8" y2="13" />{" "}
                    <line x1="16" y1="17" x2="8" y2="17" />{" "}
                    <polyline points="10 9 9 9 8 9" />
                  </svg>
                  <b>Nombre : {file.name}</b>
                  <br />
                  Tamaño : {Math.trunc(file.size / 1024)} KB (aprox)
                  <br />
                </p>
              ) : (
                <div>
                  <svg
                    aria-hidden="true"
                    className="mb-3 h-10 w-10 text-gray-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                    ></path>
                  </svg>
                  <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
                    <span className="font-semibold">Da click para subir </span>{" "}
                    o arrastra y suelta
                  </p>
                  <p className="text-xs text-gray-500 dark:text-gray-400">
                    CSV, XLS, JSON
                  </p>
                </div>
              )}
              <input
                type="file"
                accept=".csv,.xls"
                className="hidden"
                onChange={(e) => setFile(e.target.files?.[0] || null)}
              />
            </div>
          </div>
        </div>
      )}
      {error === 2 && (
        <div className="col-span-6 ml-8 mr-6 rounded-lg bg-red-100 p-2">
          <h2 className=" text-xl font-bold text-slate-800">
            <svg
              className="mb-1 mr-2 inline-block h-7 w-7"
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
              <path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2" />{" "}
              <polyline points="7 9 12 4 17 9" />{" "}
              <line x1="12" y1="4" x2="12" y2="16" />
            </svg>
            1. Sube tu catalogo
          </h2>
          <h3 className="mt-4 text-lg font-bold text-red-600">
            Ha sucedido un error!{" "}
          </h3>
          <p className="my-4 text-slate-500">
            Parece que ha habido un error procesando tu archivo, porfavor
            asegurate de que tengas la columna{" "}
            <b className="text-red-500">modelo</b>, recuerda que no debe tener
            espacios ni mayusculas.
            <br />
            <br />
            Si el error persiste, porfavore reporta el error y contacta al{" "}
            <span className="underline">soporte tecnico</span>.
          </p>
        </div>
      )}
      {error === 1 && (
        <div className="col-span-6 ml-8 mr-2">
          <h2 className=" text-xl font-bold text-slate-800">
            <svg
              className="mb-1 mr-2 inline-block h-7 w-7"
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
              <path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2" />{" "}
              <polyline points="7 9 12 4 17 9" />{" "}
              <line x1="12" y1="4" x2="12" y2="16" />
            </svg>
            1. Sube tu catalogo
          </h2>
          <p className="my-4 text-slate-500">
            Perfecto! Estamos listos para recibir tu catalogo, sin embargo, es
            importante que consideres que esta accion entrenara a{" "}
            <i className="text-violet-600">Wheelie</i>, por lo que es{" "}
            <i className="font-bold text-red-800">irreversible</i> <br />
            Al dar click en "Confirmar", estas aceptando la responsabilidad de
            tu catalogo.
          </p>
        </div>
      )}
      <div className="col-span-6 row-start-6 mx-6 items-end  justify-end text-end ">
        <button
          onClick={cancelOverride}
          className="mx-2 rounded-[2rem] border-2 border-slate-300 px-4 py-2 text-slate-400 transition-all duration-200 hover:border-red-400 hover:text-red-400"
        >
          Cancelar
        </button>
        <button
          onClick={handleSubmit}
          className="mx-2 rounded-[2rem] border-2 border-violet-500 px-4 py-2 text-violet-500 transition-all duration-200 hover:bg-violet-500 hover:text-white"
        >
          {error === 2 && "Regresar"}
          {error === 0 && "Subir"}
        </button>
      </div>
    </>
  );
}
