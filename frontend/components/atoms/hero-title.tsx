/* eslint-disable react-hooks/rules-of-hooks */
'use client';

import React from 'react';
import { useEffect, useState } from 'react';

const HeroTitle = ({
  title,
  highlight_word,
}: {
  title: string;
  highlight_word: string;
}) => {
  const [html, setHtml] = useState(title);

  useEffect(() => {
    let new_html: string | string[] = title.split(highlight_word);

    if (new_html.length > 1) {
      new_html =
        new_html[0] +
        `<span class="main-txt leading-snug">${highlight_word}</span>` +
        new_html[1];
      setHtml(new_html);
    } else {
      setHtml(title);
    }
  }, []);
  return (
    <h1
      className="text-5xl font-bold leadi sm:text-6xl leading-snug"
      dangerouslySetInnerHTML={{ __html: html }}
    ></h1>
  );
};

export default HeroTitle;
