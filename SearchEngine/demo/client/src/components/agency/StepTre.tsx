import { useEffect, useState } from "react";
import { Socket, io } from "socket.io-client";
type Props = {
  onNext: () => void;
  onCancel: (e: any) => void;
  lines: number;
  fileId: string;
  view: object;
  make: string;
};

export default function StepTre({
  onNext,
  onCancel,
  lines,
  fileId,
  view,
  make,
}: Props) {
  const [actualProgress, setActualProgress] = useState(0);
  const [socket, setSocket] = useState<Socket | null>(null);
  const [running, setRunning] = useState(true);

  const startProcess = () => {
    const socket = io("http://localhost:8082");
    socket.on("progress", (data) => {
      console.log(data);
      setActualProgress(data.number);
    });
    //The agency id shoul be changed to the agency id of the user who is uploading the cars
    socket.emit("start-processing", {
      fileId,
      view,
      make,
      agencyId: 3,
      branchId: 13,
    });
    setSocket(socket);
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

  useEffect(() => {
    if (actualProgress + 1 === lines) {
      socket?.disconnect();
      setRunning(false);
      console.log("Disconected stream server");
    }
  });

  return (
    <>
      <div className="col-span-6 ml-8 mr-2">
        <h2 className="text-xl font-bold text-slate-800">
          <svg
            className="mb-[0.2rem] mr-2 inline-block h-7 w-7"
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
            <line x1="12" y1="12" x2="12" y2="12.01" />{" "}
            <path
              d="M12 2a4 10 0 0 0 -4 10a4 10 0 0 0 4 10a4 10 0 0 0 4 -10a4 10 0 0 0 -4 -10"
              transform="rotate(45 12 12)"
            />{" "}
            <path
              d="M12 2a4 10 0 0 0 -4 10a4 10 0 0 0 4 10a4 10 0 0 0 4 -10a4 10 0 0 0 -4 -10"
              transform="rotate(-45 12 12)"
            />
          </svg>
          3. Deja que Wheelie haga su magia.
        </h2>
        <p className="mr-2 mt-4 text-slate-500">
          Wheelie tiene tu archivo! Ahora solo da click en el boton de "Empezar"
          para que Wheelie analize cada vehciulo en tu archivo. Porfavor, no
          cierres esta ventana.
          <br />
          <br />
          <span className="text-xs">
            * Toma en cuenta que al dar click en "Empezar", aceptas que este es
            una accion <i>irreversible</i> y asumes la responsabilidad de la
            misma.
          </span>
        </p>
      </div>
      <div className="col-span-4 col-start-2 items-center justify-center text-center ">
        {actualProgress === 0 && (
          <button
            onClick={startProcess}
            className="rounded-md bg-blue-500 px-4 py-2 font-bold text-white transition-all duration-300 hover:scale-110 active:bg-blue-800"
          >
            Empezar
          </button>
        )}
        {actualProgress !== 0 && (
          <>
            <div className="mb-1 flex justify-between">
              <span className="text-base font-medium text-blue-800 dark:text-white">
                Columnas Procesadas
              </span>
              <span className="text-sm font-medium text-blue-800 dark:text-white">
                {Math.ceil((actualProgress * 100) / lines)} %
                {actualProgress + 1 === lines && " Completo!"}
              </span>
            </div>
            <div className="h-2.5 rounded-full bg-gray-200 dark:bg-gray-700">
              <div
                className="h-2.5 rounded-full bg-blue-500"
                style={{ width: `${(actualProgress * 100) / lines}%` }}
              ></div>
            </div>
          </>
        )}
      </div>
      <div className="col-span-6 row-start-6 mx-6 items-end  justify-end text-end ">
        <button
          onClick={cancelOverride}
          disabled={!(actualProgress === 0)}
          className={`mx-2 rounded-[2rem] border-2 border-slate-300 px-4 py-2 text-slate-400 transition-all duration-200 ${
            actualProgress === 0
              ? "hover:border-red-400 hover:text-red-400"
              : ""
          } `}
        >
          Cancelar
        </button>
        <button
          onClick={onNext}
          disabled={running}
          className={`mx-2 rounded-[2rem] border-2 border-blue-500 px-4 py-2 text-blue-500 transition-all duration-200 ${
            running ? "" : "hover:bg-blue-500 hover:text-white"
          } `}
        >
          Continuar
        </button>
      </div>
    </>
  );
}
