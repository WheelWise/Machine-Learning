import Link from "next/link";
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <section className="">
        <div className="mx-auto max-w-screen-xl px-4 py-8 text-center lg:py-16">
          <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
            <i className="text-[#755ee9]">WheelWise</i>{" "}
            <span className="lg:text-[3.7rem]">Search Engine</span>
          </h1>
          <p className="mb-8 text-lg font-normal text-gray-500 dark:text-gray-400 sm:px-16 lg:px-48 lg:text-xl">
            This is just a quick demo and a playgroud to show how the search
            engine works, also works as a place to expermient with new features
            and tests.
          </p>
          <div className="flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-x-4 sm:space-y-0">
            <Link
              href="/customer"
              className="inline-flex items-center justify-center rounded-lg bg-violet-500 px-5 py-3 text-center text-base font-medium text-white transition-all duration-300 hover:scale-110 hover:bg-violet-700 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900"
            >
              Customer
              <svg
                aria-hidden="true"
                className="-mr-1 ml-2 h-5 w-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fillRule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clipRule="evenodd"
                ></path>
              </svg>
            </Link>
            <Link
              href="/agency"
              className="inline-flex items-center justify-center rounded-lg bg-violet-500 px-5 py-3 text-center text-base font-medium text-white transition-all duration-300 hover:scale-110 hover:bg-violet-700 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900"
            >
              Seller
              <svg
                aria-hidden="true"
                className="-mr-1 ml-2 h-5 w-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fillRule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clipRule="evenodd"
                ></path>
              </svg>
            </Link>
            <a
              href="https://github.com/WheelWise/Machine-Learning/tree/main/SearchEngine"
              className="inline-flex items-center justify-center rounded-lg border border-gray-300 px-5 py-3 text-center text-base font-medium text-gray-900 transition-all duration-300 hover:scale-110 hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-800"
            >
              Learn more
            </a>
          </div>
        </div>
      </section>
    </main>
  );
}
