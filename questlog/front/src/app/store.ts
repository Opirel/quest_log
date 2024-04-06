import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import QuestReducer from '../features/quests/questSlice';
import counterReducer from '../features/counter/counterSlice';

export const store = configureStore({
  reducer: {
    Quest:QuestReducer,
    counter:counterReducer
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
