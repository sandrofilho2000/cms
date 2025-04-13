import api from '@/app/api/route';
import HomeMain from '@/components/organisms/HomeMain';
import site_data_default from "@/public/site_data_default.json";

export default async function Home({ params }: { params: { lid: string } }) {
  let site_data = await api(`site_data/${params.lid}`) || site_data_default
  return <HomeMain site_data={site_data} />;
}
