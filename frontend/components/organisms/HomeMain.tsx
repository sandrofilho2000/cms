'use client';
import Hero from '@/components/organisms/Hero';
import { iSiteData } from '@/interfaces';
import RootStyles from '../RootStyles';
import Banner from './Banner';
import Faq from './Faq';
import Features from './Features';
import Stats from './Stats';

const HomeMain = ({ site_data }: {site_data:iSiteData}) => {
  return (
    <main className="">
      <RootStyles data={site_data.color} />
      <Hero data={site_data.hero} />
      <Stats data={site_data.stats} />
      <Features data={site_data.features} />
      <Banner data={site_data.banner} />
      <Faq data={site_data.faq} />
    </main>
  );
};

export default HomeMain;
