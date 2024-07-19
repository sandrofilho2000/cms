import { Button } from '@/components/atoms/button';
import Image from 'next/image';
import Link from 'next/link';
import HeroTitle from '../atoms/hero-title';
import InstallCode from '../installcode';
import { iHero } from '@/interfaces';

const Hero = ({ data }: { data: iHero }) => {
  const { title, highlight_word, text, cta_link, cta_text, command_line, img } =
    data;
  return (
    <section className="">
      <div className="max-w-7xl flex flex-col justify-center p-1 md:px-10 mx-auto sm:pt-10 lg:flex-row lg:justify-between items-center">
        <div className="flex flex-col justify-center p-6 text-center rounded-sm lg:max-w-md xl:max-w-lg lg:text-left leading-snug">
          <HeroTitle
            title={title}
            highlight_word={highlight_word}
          />
          <p className="mt-6 mb-8 text-lg sm:mb-12 leading-snug">{text}</p>{' '}
          <div className="flex justify-center items-center md:justify-start w-full">
            <div className="mb-8 text-lg leading-snug">
              <InstallCode installation={command_line} />
            </div>
          </div>
          <div className="flex flex-col space-y-4 sm:items-center sm:justify-center sm:flex-row sm:space-y-0 sm:space-x-4 lg:justify-start">
            <Link href={cta_link}>
              <Button className="">{cta_text}</Button>
            </Link>
          </div>
        </div>
        <div className="flex items-center justify-center p-6 mt-8 lg:mt-0 h-72 sm:h-80 lg:h-96 xl:h-112 2xl:h-128 ">
          <Image
            src={
              img
                ? `http://localhost:8000${img}`
                : 'https://images.unsplash.com/photo-1543269664-76bc3997d9ea?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            }
            alt=""
            height={500}
            width={500}
            className="rounded-sm"
          />
        </div>
      </div>
    </section>
  );
};

export default Hero;
