type Props = {
  car: any;
  view: any;
};
export default function CarCard({ car, view }: Props) {
  return (
    <div className="col-span-1 overflow-y-auto rounded-lg border border-gray-200 bg-white shadow-lg dark:border-gray-700 dark:bg-gray-800">
      <div className="w-full">
        <img
          className="rounded-t-lg p-8 "
          src="https://www.ford.com/cmslibs/content/dam/vdm_ford/live/en_us/ford/nameplate/fusion/2020/collections/3-2/20_frd_fsn_ps34_sel_mgnt_32.jpg/_jcr_content/renditions/cq5dam.web.1440.1440.jpeg"
          alt="product image"
        />
      </div>
      <div className="px-5 pb-5">
        <a href="#">
          <h5 className="text-xl font-semibold tracking-tight text-gray-900 dark:text-white">
            {car["marca"]} {car[view["title"]]} {car[view["year"]]}
          </h5>
        </a>
        <div className="flex items-center justify-between">
          <span className="text-2xl font-bold text-gray-900 dark:text-white">
            ${car[view["price"]]} MXN
          </span>
          <a
            href="#"
            className="rounded-lg bg-blue-700 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Ver Mas
          </a>
        </div>
      </div>
    </div>
  );
}
