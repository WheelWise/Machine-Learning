import { CatalogUploader, CatalogTable } from "@/components/agency";

export default function Agency() {
  return (
    <main className="ml-8 mt-8 grid grid-cols-12 gap-3 text-gray-800">
      <h1 className="col-span-12 text-2xl font-bold md:text-4xl lg:text-5xl">
        Catalogo
      </h1>
      <hr className="col-span-8 mt-3 w-full border-violet-200 bg-black" />
      <CatalogTable />
      <div className="col-span-4 mr-10 items-end justify-end text-end">
        <h2 className="text-2xl font-semibold">Herramientas</h2>
        <hr className="float-right my-4 mt-3 w-[80%] border-violet-200 bg-black" />
        <CatalogUploader />
      </div>
    </main>
  );
}
