import { iFaq, iFaqItem } from '@/interfaces';
import React from 'react';

const FaqItem = ({ data }: { data: iFaqItem }) => {
  return (
    <details className="w-full border rounded-lg">
      <summary className="px-4 py-6 focus:outline-none focus-visible:ri">
        {data.question}
      </summary>
      <p className="px-4 py-6 pt-0 ml-4 -mt-4 ">{data.answer}</p>
    </details>
  );
};

export default FaqItem;
