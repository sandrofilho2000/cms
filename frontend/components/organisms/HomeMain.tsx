'use client';
import React, { useEffect } from 'react';
import { Button } from '@/components/atoms/button';
import Image from 'next/image';
import Link from 'next/link';
import Hero from '@/components/organisms/Hero';
import { useSiteData } from '@/context/sitedataContext';
import Stats from './Stats';
import Features from './Features';
import Banner from './Banner';
import Faq from './Faq';
const HomeMain = ({ site_data }: any) => {
  const { siteData, setSiteData }: any = useSiteData();

  useEffect(() => {
    setSiteData(site_data);
  }, []);

  return (
    <main className="">
      <Hero data={site_data.hero} />
      <Stats data={site_data.stats} />
      <Features data={site_data.features} />
      <Banner data={site_data.banner} />
      <Faq data={site_data.faq} />
    </main>
  );
};

export default HomeMain;
