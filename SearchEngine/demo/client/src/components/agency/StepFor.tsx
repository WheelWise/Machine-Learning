import { Wheelie } from "@/assets";
import Image from "next/image";

type Props = {
  onCancel: (e: any) => void;
};

export default function StepFor({ onCancel }: Props) {
  return (
    <>
      <div className="col-span-6 grid grid-cols-2 ">
        <div className="col-span-1 ml-8 mr-2">
          <h2 className=" text-xl font-bold text-slate-800">
            <svg
              className="mb-[0.3rem] mr-2 inline-block h-7 w-7"
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
              <path d="M9 5H7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2V7a2 2 0 0 0 -2 -2h-2" />{" "}
              <rect x="9" y="3" width="6" height="4" rx="2" />{" "}
              <line x1="9" y1="12" x2="9.01" y2="12" />{" "}
              <line x1="13" y1="12" x2="15" y2="12" />{" "}
              <line x1="9" y1="16" x2="9.01" y2="16" />{" "}
              <line x1="13" y1="16" x2="15" y2="16" />
            </svg>
            4. Resultados.
          </h2>
          <div
            className={` mt-4s mx-auto w-[70%] rounded-md border-2  border-dashed border-slate-200 p-6`}
          >
            <Image src={Wheelie} alt="Wheelie" />
          </div>
        </div>
        <div className="col-span-1 ">
          <p className="mr-6 mt-10 text-slate-500">
            Felicidades! <i className="text-blue-600">Wheelie</i> Ha aprendido y
            analizado el archivo que le diste, ahora tus vehiculos apareceran en
            las busquedas de todos los usuarios. <br /> <br />
            <span className="text-xs ">
              Los autos se han añadidos al dashboard de tu catalogo, usalo
              sabiamente para administrar tus vehiculos.
            </span>
          </p>
        </div>
      </div>
      <div className="col-span-6 row-start-6 mx-6 items-end  justify-end text-end ">
        <button
          onClick={onCancel}
          className="mx-2 rounded-[2rem] border-2 border-blue-500 px-4 py-2 text-blue-500 transition-all duration-200 hover:bg-blue-500 hover:text-white"
        >
          Aceptar
        </button>
      </div>
    </>
  );
}
