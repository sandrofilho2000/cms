import React from 'react';
import { Button } from '../atoms/button';
import Link from 'next/link';
import { iBanner } from '@/interfaces';

const Banner = ({ data }: { data: iBanner }) => {
  return (
    <section className="py-6 main-bg text-gray-50 mt-14">
      <div className="container justify-center p-4 mx-auto space-y-8 md:p-10 lg:space-y-0 lg:space-x-12 lg:justify-around lg:flex lg:flex-row">
        <div className="flex flex-col space-y-2 text-center lg:text-left">
          <h2 className="text-3xl font-bold leading-none">{data.title}</h2>
          <p className="px-4 text-lg lg:px-0"> {data.subtitle} </p>
        </div>
        <div className="flex flex-row items-center self-center justify-center flex-shrink-0 lg:justify-end">
          <Link
            target="_blank"
            href={data.cta_link}
          >
            <Button
              variant="outline"
              size="lg"
              className="text-black dark:text-white"
            >
              {data.cta_text}
            </Button>
          </Link>
        </div>
      </div>
    </section>
  );
};

export default Banner;
