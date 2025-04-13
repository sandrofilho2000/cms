'use client';

export default function RootStyles({data}:{data:string}) {

  return (
    <>
      <style
        jsx
        global
      >
        {`
          :root {
            --main-color: ${data};
          }

          .main-bg {
            background-color: var(--main-color);
          }

          .main-txt {
            color: var(--main-color);
          }
        `}
      </style>
    </>
  );
}
