import { iStat } from '@/interfaces';
import React from 'react';

const Stat = ({ item }: { item: iStat }) => {
  return (
    <div className="flex p-4 space-x-4 rounded-lg md:space-x-6  ">
      <div
        className="flex justify-center p-2 align-middle rounded-lg sm:p-4 main-bg text-gray-100 text-2xl"
        dangerouslySetInnerHTML={{ __html: item.icon }}
      />
      <div className="flex flex-col justify-center align-middle">
        <p className="text-3xl font-semibold leadi">{item.big_number}</p>
        <p className="capitalize">{item.title}</p>
      </div>
    </div>
  );
};

export default Stat;
