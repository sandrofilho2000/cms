import { iFeature } from '@/interfaces';
import Image from 'next/image';
import React from 'react';
import Feature from '../cells/Feature';

const Features = ({ data }: { data: iFeature[] }) => {
  return (
    <section className="lg:p-8">
      <div className="md:container px-2 mx-auto space-y-20 lg:space-y-36">
        {data.map((item, index: number) => (
          <Feature
            key={index}
            item={item}
          />
        ))}
      </div>
    </section>
  );
};

export default Features;
