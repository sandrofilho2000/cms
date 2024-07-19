import HomeMain from '@/components/organisms/HomeMain';
import axios from 'axios';
import { GetServerSideProps, NextApiRequest } from 'next';

async function api(path: string) {
  let url = `http://127.0.0.1:8000/api/${path}`;
  try {
    const res = await axios.get(url);
    return res.data;
  } catch (error) {
    console.error('Erro na requisição:', error);
    throw error;
  }
}

export default async function Home({ params }: { params: { lid: string } }) {
  const site_data = await api(`site_data/${params.lid}`);
  return <HomeMain site_data={site_data} />;
}
