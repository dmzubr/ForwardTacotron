from utils.text import text_to_sequence, sequence_to_text, to_sova_phonemes


if __name__ == '__main__':
    txt_to_check = 'Назначенный исполнитель'
    print(txt_to_check)
    sova_phonems_txt = to_sova_phonemes(txt_to_check)
    print(f'SOVA phonemication res is: {sova_phonems_txt}')
    seq = text_to_sequence(sova_phonems_txt)
    print(f'Text to seq is:')
    print(seq)
    reversed = sequence_to_text(seq)
    print(f'Reversed txt is: {reversed}')

    txt_to_check = 'Назначенный исполнитель свяжется? с вами для решения вашей проблемы!'
    print(txt_to_check)
    p = to_sova_phonemes(txt_to_check)
    #print(p)
