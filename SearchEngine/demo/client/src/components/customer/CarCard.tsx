type Props = {
  car: any;
  view: any;
  image: any;
};

const colors = {
  Rojo: "bg-red-600",
  Blanco: "bg-white",
  Negro: "bg-black",
  Gris: "bg-slate-300",
  Azul: "bg-blue-500",
};
export default function CarCard({ car, view, image }: Props) {
  return (
    <div className="col-span-1 overflow-hidden rounded-lg bg-white shadow-md transition-all duration-300 hover:-translate-y-4 hover:shadow-2xl">
      <div className="relative" style={{ paddingBottom: "75%" }}>
        <img
          src={image}
          alt="Foto del carro"
          className="absolute inset-0 h-full w-full object-cover"
        />
      </div>
      <div className="p-4">
        <h3 className="text-xl font-bold">
          {" "}
          {car["marca"]} {car[view["title"]]} {car[view["year"]]}
        </h3>
        <div className="w-[70%] overflow-hidden overflow-ellipsis text-gray-500 ">
          <span className="align-middle"> ${car[view["price"]]} MXN</span>
          <div
            className={`ml-16 inline-block h-5 w-5 rounded-full border-2 border-slate-600 ${
              colors[car["color"]]
            } align-middle`}
          ></div>
        </div>
      </div>
    </div>
  );
}
