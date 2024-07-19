import { iFeature } from '@/interfaces';
import Image from 'next/image';
import React from 'react';

const Feature = ({ item }: { item: iFeature }) => {
  return (
    <div className="flex flex-col max-w-xl mx-auto overflow-hidden rounded-md lg:max-w-full feature--card min-h-96">
      <div className="flex items-center justify-center flex-1 px-4 mb-8 lg:flex-3 h-72 lg:justify-start sm:h-80 lg:h-96 lg:mb-0">
        <Image
          src={
            item.img
              ? `http://localhost:8000${item.img}`
              : 'https://images.unsplash.com/photo-1543269664-76bc3997d9ea?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
          }
          alt=""
          height={500}
          width={500}
          className="rounded-sm"
        />
      </div>
      <div className="flex flex-col justify-center flex-1 px-6 lg:flex-2">
        <span className="mb-2 text-xs tracking-widest uppercase main-txt">
          {' '}
          {item.subtitle}{' '}
        </span>
        <h2 className="text-3xl font-bold"> {item.title} </h2>
        <p className="my-6 "> {item.text} </p>
      </div>
    </div>
  );
};

export default Feature;
