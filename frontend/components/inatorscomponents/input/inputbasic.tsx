import { Input } from '@/components/atoms/input';
import { Label } from '@/components/atoms/label';
import React from 'react';

const Inputbasic = () => {
  return (
    <div>
      <form
        action=""
        className="w-max mx-auto"
      >
        <Label>Name</Label>
        <Input
          type="text"
          placeholder="Enter your name"
        />
      </form>
    </div>
  );
};

export default Inputbasic;
