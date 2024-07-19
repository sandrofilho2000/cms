'use client';
import { createContext, useContext, useState, useEffect } from 'react';

const sitedataContext = createContext({});

export const useSiteData = () => useContext(sitedataContext);

export const SitedataContextProvider = ({ children }) => {
  const [siteData, setSiteData] = useState({});

  return (
    <sitedataContext.Provider
      value={{
        setSiteData,
        siteData,
      }}
    >
      {children}
    </sitedataContext.Provider>
  );
};
