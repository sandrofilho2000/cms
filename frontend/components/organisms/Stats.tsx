import React from 'react';
import Stat from '../cells/Stat';
import { iStat } from '@/interfaces';

const Stats = ({ data }: { data: iStat[] }) => {
  return (
    data?.length && (
      <section className="p-6 my-6">
        <div className="container grid grid-cols-1 gap-6 mx-auto sm:grid-cols-2 xl:grid-cols-4">
          {data.map((item: iStat, index: number) => (
            <Stat
              item={item}
              key={index}
            />
          ))}
        </div>
      </section>
    )
  );
};

export default Stats;
