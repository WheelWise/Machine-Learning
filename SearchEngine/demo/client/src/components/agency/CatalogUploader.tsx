"use client";
import React, { useState } from "react";
import axios from "axios";
import StepList from "./StepList";
import StepOne from "./StepOne";
import StepTwo from "./StepTwo";
import StepTre from "./StepTre";

export default function CatalogUploader() {
  const [open, setOpen] = useState(false);
  const [actualStep, setActualStep] = useState(0);

  const [fileId, setFileId] = useState("");
  const [fileLines, setFileLines] = useState(2);

  function handleModal(e: any) {
    e.preventDefault();
    setOpen(!open);
    setActualStep(0);
  }

  function handleNext() {
    setActualStep((prevStep) => prevStep + 1);
  }

  return (
    <>
      <button
        onClick={handleModal}
        data-modal-target="defaultModal"
        data-modal-toggle="defaultModal"
        className="tranistion-all group rounded-md bg-indigo-900 py-2 pl-6 pr-14 text-white duration-300 hover:scale-110"
      >
        <svg
          className="mr-6 inline-block h-6 w-6 text-white transition-all duration-500 group-hover:rotate-180"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          {" "}
          <circle cx="12" cy="12" r="10" />{" "}
          <line x1="12" y1="8" x2="12" y2="16" />{" "}
          <line x1="8" y1="12" x2="16" y2="12" />
        </svg>
        Subir Catalogo
      </button>

      <div
        className={` transition-opacity duration-300 ${
          !open
            ? "pointer-events-none opacity-0 "
            : "pointer-events-auto opacity-100"
        }`}
      >
        <div className="z-1 fixed -left-0 top-0 grid h-full w-full grid-cols-12  bg-slate-600 bg-opacity-90">
          <div className=" z-10  col-span-8 col-start-3 my-[8rem] grid grid-cols-6  rounded-2xl bg-white text-start shadow-lg">
            <h1 className="col-span-6 row-span-1 m-8 mb-0 text-2xl font-bold ">
              Añade vehiculos a tu catalogo
            </h1>
            <div className="col-span-6 items-center justify-center text-center">
              <StepList step={actualStep} />
            </div>
            {actualStep === 0 && (
              <StepOne
                onNext={handleNext}
                onCancel={handleModal}
                lineSetter={setFileLines}
                fileIdSetter={setFileId}
              />
            )}

            {actualStep === 1 && (
              <StepTwo
                onNext={handleNext}
                onCancel={handleModal}
                lines={fileLines}
                fileId={fileId}
              />
            )}
            {actualStep === 2 && <StepTre onCancel={handleModal} />}
          </div>
        </div>
      </div>
    </>
  );
}
