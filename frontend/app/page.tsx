import HomeMain from '@/components/organisms/HomeMain';
import site_data_default from "@/public/site_data_default.json";
import api from './api/route';

export default async function Home() {
  let site_data = await api('site_data') || site_data_default
  return <HomeMain site_data={site_data} />;
}
