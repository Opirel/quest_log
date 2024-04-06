import React, { useState, ChangeEvent } from 'react';
import { useAppDispatch } from '../../app/hooks';
import { QuestAsync } from './questSlice';

export function Quest() {
  const dispatch = useAppDispatch();

  const [QName, setQName] = useState<string>("");
  const [QDescription, setQDescription] = useState<string>("");
  const [QCompleted, setQCompleted] = useState<boolean>(false);
  const [Qreward, setQreward] = useState<string>("");
  const [QpcInvolved, setQpcInvolved] = useState<string[]>([]);

  const characters = [
    { id: '1', name: 'Urthor' },
    { id: '2', name: 'Aelin' },
    { id: '3', name: 'Brol' },
    { id: '4', name: 'Leonard' },
    { id: '5', name: 'Levy' },
    { id: '6', name: 'Musashi' }
  ];

  const handleCompletionChange = (e: ChangeEvent<HTMLInputElement>) => {
    setQCompleted(e.target.checked);
  };

  const handleCharactersChange = (e: ChangeEvent<HTMLSelectElement>) => {
    const selectedOptions = Array.from(e.target.selectedOptions, option => option.value);
    setQpcInvolved(selectedOptions);
  };


  const handleSubmit = () => {
    const payload = {
  quest_name: QName,
  description: QDescription, // Align this and other fields with your Django model
  completed: QCompleted,
  reward: Qreward,
  pc_involved: QpcInvolved
}
    dispatch(QuestAsync(payload));
  };
  return (
    <div>
      <div>
        <div>Quest Log</div>
        Quest Name: <input value={QName} onChange={(e) => setQName(e.target.value)} /><br />
        Quest Description: <input value={QDescription} onChange={(e) => setQDescription(e.target.value)} /><br />
        Completed: <input type="checkbox" checked={QCompleted} onChange={handleCompletionChange} /><br />
        Quest Reward: <input value={Qreward} onChange={(e) => setQreward(e.target.value)} /><br />
        Characters Involved:
        <select multiple={true} value={QpcInvolved} onChange={handleCharactersChange}>
          {characters.map((character) => (
            <option key={character.id} value={character.id}>{character.name}</option>
          ))}
        </select><br />
        <button onClick={handleSubmit}>Send</button>
      </div>
    </div>
  );
}
