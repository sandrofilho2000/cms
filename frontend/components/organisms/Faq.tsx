import { iFaq } from '@/interfaces';
import React from 'react';
import FaqItem from '../cells/FaqItem';

const Faq = ({ data }: { data: iFaq }) => {
  return (
    <section className="mt-14 md:max-w-[70vw] mx-auto">
      <div className="container flex flex-col justify-center px-4 py-8 mx-auto md:p-8">
        <h2 className="text-2xl font-semibold sm:text-4xl">{data.title}</h2>
        <p className="mt-4 mb-8 ">{data.subtitle}</p>
        <div className="space-y-4">
          {data.questions.map((item, index) => (
            <FaqItem
              data={item}
              key={index}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Faq;
