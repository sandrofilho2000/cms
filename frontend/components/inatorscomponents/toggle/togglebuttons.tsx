import { Input } from '@/components/atoms/input';
import { Label } from '@/components/atoms/label';
import React from 'react';

const Togglebuttons = () => {
  return (
    <div>
      <Label className="inline-flex items-center p-2 rounded-md cursor-pointer text-white">
        <Input
          id="Toggle3"
          type="checkbox"
          className="hidden peer "
        />
        <span className="px-4 py-3 rounded-l-md main-bg peer-checked:bg-black">
          Monthly
        </span>
        <span className="px-4 py-3 rounded-r-md bg-black peer-checked:main-bg">
          Annually
        </span>
      </Label>
    </div>
  );
};

export default Togglebuttons;
