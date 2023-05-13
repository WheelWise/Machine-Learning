type Props = {
  step: number;
};

export default function StepList(props: Props) {
  return (
    <ol className=" ml-[14%] flex w-full items-center">
      <li
        className={`text flex w-full items-center transition-all duration-500 ${
          props.step > 0 ? "text-blue-600" : "text-gray-400"
        } after:inline-block after:h-1 after:w-full after:border-4 after:border-b ${
          props.step > 0 ? "after:border-blue-100" : "after:border-gray-100"
        } after:content-[''] dark:text-blue-500 dark:after:border-blue-800`}
      >
        <span
          className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${
            props.step > 0 ? "bg-blue-100" : "bg-gray-100"
          } dark:bg-blue-800 lg:h-12 lg:w-12`}
        >
          <svg
            className={`h-5 w-5 ${
              props.step > 0 ? "text-blue-600" : "text-gray-400"
            }`}
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
        </span>
      </li>
      <li
        className={`text flex w-full items-center transition-colors duration-500 ${
          props.step > 1 ? "text-blue-600" : "text-gray-400"
        } after:inline-block after:h-1 after:w-full after:border-4 after:border-b ${
          props.step > 1 ? "after:border-blue-100" : "after:border-gray-100"
        } after:content-[''] dark:text-blue-500 dark:after:border-blue-800`}
      >
        <span
          className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${
            props.step > 1 ? "bg-blue-100" : "bg-gray-100"
          } dark:bg-blue-800 lg:h-12 lg:w-12`}
        >
          <svg
            className={`h-7 w-7 ${
              props.step > 1 ? "text-blue-600" : "text-gray-400"
            }`}
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
        </span>
      </li>
      <li className="flex w-full items-center">
        <span
          className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${
            props.step > 2 ? "bg-blue-100" : "bg-gray-100"
          } dark:bg-blue-800 lg:h-12 lg:w-12`}
        >
          <svg
            aria-hidden="true"
            className={`h-5 w-5 ${
              props.step > 2 ? "text-blue-600" : "text-gray-400"
            }`}
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path>
            <path
              fillRule="evenodd"
              d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm9.707 5.707a1 1 0 00-1.414-1.414L9 12.586l-1.293-1.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            ></path>
          </svg>
        </span>
      </li>
    </ol>
  );
}
