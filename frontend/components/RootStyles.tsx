'use client';
import { useSiteData } from '@/context/sitedataContext';
import { useEffect, useState } from 'react';

export default function RootStyles() {
  const [mainColor, setMainColor] = useState('');
  const { siteData }: any = useSiteData();
  useEffect(() => {
    setMainColor(
      siteData?.color_palette?.main_color
        ? siteData.color_palette.main_color
        : '#020817'
    );
  }, [siteData]);

  return (
    <>
      <style
        jsx
        global
      >
        {`
          :root {
            --main-color: ${mainColor};
          }

          .main-bg {
            background-color: var(--main-color);
          }

          .main-txt {
            color: var(--main-color);
          }
        `}
      </style>
    </>
  );
}
